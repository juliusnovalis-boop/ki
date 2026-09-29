' Migration des marques et modèles vers un catalogue premium.
' Les clés primaires restent stables : les réservations et les voitures restent liées.
' Lancer après avoir fermé Access. Sauvegarde automatique avant toute modification.
Option Explicit

Const dbFailOnError = 128

Dim fso, scriptDir, databasePath, backupPath, stamp, engine, workspace, db
Dim marqueIds, marqueNoms, modeleIds, modeleNoms, modeleMarqueIds
Dim i, sql, errText, backupName
Set fso = Nothing
Set engine = Nothing
Set workspace = Nothing
Set db = Nothing

marqueIds = Array( _
    1, 2, 3, 4, 5)

marqueNoms = Array( _
    "Ferrari", "Lamborghini", "Bentley", "Bugatti", "Rolls-Royce")

modeleIds = Array( _
    1, 2, 3, 4, 5, _
    6, 7, 8, 9, 10, _
    11, 12, 13, 14, 15, _
    16, 17, 18, 19, 20, _
    21, 22, 23, 24, 25, _
    26, 27, 28, 29, 30, _
    31, 32, 33, 34, 35, _
    36, 37, 38, 39, 40, _
    41, 42, 43, 44, 45, _
    46, 47, 48, 49, 50, _
    51, 52, 53, 54, 55, _
    56, 57, 58, 59, 60)

modeleNoms = Array( _
    "Ferrari Roma", "Lamborghini Urus SE", "Bentley Continental GT", "Bugatti Chiron", "Rolls-Royce Phantom", _
    "Ferrari 296 GTB", "Lamborghini Revuelto", "Bentley Continental GTC", "Bugatti Chiron Sport", "Rolls-Royce Ghost", _
    "Ferrari 296 GTS", "Lamborghini Temerario", "Bentley Flying Spur", "Bugatti Chiron Pur Sport", "Rolls-Royce Cullinan", _
    "Ferrari Purosangue", "Lamborghini Huracán Tecnica", "Bentley Bentayga", "Bugatti Chiron Super Sport", "Rolls-Royce Spectre", _
    "Ferrari 12Cilindri", "Lamborghini Huracán Sterrato", "Bentley Bentayga EWB", "Bugatti Divo", "Rolls-Royce Dawn", _
    "Ferrari 12Cilindri Spider", "Lamborghini Huracán STO", "Bentley Continental GT Speed", "Bugatti Centodieci", "Rolls-Royce Wraith", _
    "Ferrari SF90 Stradale", "Lamborghini Urus Performante", "Bentley Bentayga Speed", "Bugatti Bolide", "Rolls-Royce Cullinan Black Badge", _
    "Ferrari SF90 Spider", "Lamborghini Aventador SVJ", "Bentley Flying Spur Speed", "Bugatti W16 Mistral", "Rolls-Royce Ghost Extended", _
    "Ferrari F8 Tributo", "Lamborghini Sián FKP 37", "Bentley Bacalar", "Bugatti Veyron 16.4", "Rolls-Royce Phantom Extended", _
    "Ferrari Portofino M", "Lamborghini Huracán EVO Spyder", "Bentley Batur", "Bugatti Veyron Super Sport", "Rolls-Royce Wraith Black Badge", _
    "Ferrari 812 Competizione", "Lamborghini Aventador Ultimae", "Bentley Continental GT Mulliner", "Bugatti La Voiture Noire", "Rolls-Royce Black Badge Ghost", _
    "Ferrari Daytona SP3", "Lamborghini Countach LPI 800-4", "Bentley Flying Spur Mulliner", "Bugatti Tourbillon", "Rolls-Royce Boat Tail")

modeleMarqueIds = Array( _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5, _
    1, 2, 3, 4, 5)

Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
If WScript.Arguments.Count > 0 Then
    databasePath = fso.GetAbsolutePathName(WScript.Arguments(0))
Else
    databasePath = fso.BuildPath(fso.GetAbsolutePathName(fso.BuildPath(scriptDir, "..\..")), "Database20.accdb")
End If

If Not fso.FileExists(databasePath) Then
    Fail "Base de données introuvable : " & databasePath
End If

stamp = CStr(Year(Now)) & TwoDigits(Month(Now)) & TwoDigits(Day(Now)) & "-" & _
        TwoDigits(Hour(Now)) & TwoDigits(Minute(Now)) & TwoDigits(Second(Now))
backupName = fso.GetBaseName(databasePath) & ".avant-parc-premium-" & stamp & "." & fso.GetExtensionName(databasePath)
backupPath = fso.BuildPath(fso.GetParentFolderName(databasePath), backupName)

On Error Resume Next
fso.CopyFile databasePath, backupPath, False
If Err.Number <> 0 Then
    errText = Err.Description
    Err.Clear
    On Error GoTo 0
    Fail "Impossible de créer la sauvegarde. Fermez Access et vérifiez les droits d'écriture. " & errText
End If

Set engine = CreateObject("DAO.DBEngine.120")
If Err.Number <> 0 Then
    Err.Clear
    Set engine = CreateObject("DAO.DBEngine.160")
End If
If Err.Number <> 0 Then
    errText = Err.Description
    Err.Clear
    On Error GoTo 0
    Fail "DAO/Access Database Engine est introuvable sur ce poste. Installez Access ou le moteur Access Database Engine. " & errText
End If

Set workspace = engine.Workspaces(0)
Set db = workspace.OpenDatabase(databasePath, False, False)
If Err.Number <> 0 Then
    errText = Err.Description
    Err.Clear
    On Error GoTo 0
    Fail "Impossible d'ouvrir la base. Fermez Access et vérifiez le chemin. " & errText
End If

workspace.BeginTrans
If Err.Number <> 0 Then
    errText = Err.Description
    Err.Clear
    On Error GoTo 0
    Fail "Impossible de démarrer la transaction. " & errText
End If

For i = 0 To UBound(marqueIds)
    sql = "UPDATE [Marque] SET [Marque] = '" & Replace(marqueNoms(i), "'", "''") & _
          "' WHERE [IdMarque] = " & CStr(marqueIds(i))
    Err.Clear
    db.Execute sql, dbFailOnError
    If Err.Number <> 0 Then
        errText = Err.Description
        Err.Clear
        workspace.Rollback
        On Error GoTo 0
        Fail "Erreur lors de la mise à jour des marques : " & errText
    End If
    If db.RecordsAffected <> 1 Then
        workspace.Rollback
        On Error GoTo 0
        Fail "La marque d'identifiant " & CStr(marqueIds(i)) & " n'existe pas exactement une fois. Aucune modification conservée."
    End If
Next

For i = 0 To UBound(modeleIds)
    sql = "UPDATE [Modele] SET [Modele] = '" & Replace(modeleNoms(i), "'", "''") & _
          "', [Marque] = " & CStr(modeleMarqueIds(i)) & " WHERE [IdModele] = " & CStr(modeleIds(i))
    Err.Clear
    db.Execute sql, dbFailOnError
    If Err.Number <> 0 Then
        errText = Err.Description
        Err.Clear
        workspace.Rollback
        On Error GoTo 0
        Fail "Erreur lors de la mise à jour des modèles : " & errText
    End If
    If db.RecordsAffected <> 1 Then
        workspace.Rollback
        On Error GoTo 0
        Fail "Le modèle d'identifiant " & CStr(modeleIds(i)) & " n'existe pas exactement une fois. Aucune modification conservée."
    End If
Next

workspace.CommitTrans
If Err.Number <> 0 Then
    errText = Err.Description
    Err.Clear
    workspace.Rollback
    On Error GoTo 0
    Fail "La validation de la transaction a échoué : " & errText
End If

db.Close
On Error GoTo 0
WScript.Echo "Catalogue premium appliqué : 5 marques et 60 modèles." & vbCrLf & _
             "Les identifiants sont conservés. Les tarifs, réservations et fiches clients n'ont pas été modifiés." & vbCrLf & _
             "Sauvegarde : " & backupPath

Function TwoDigits(value)
    TwoDigits = Right("0" & CStr(value), 2)
End Function

Sub Fail(message)
    On Error Resume Next
    If Not workspace Is Nothing Then workspace.Rollback
    If Not db Is Nothing Then db.Close
    On Error GoTo 0
    WScript.Echo "ERREUR : " & message
    WScript.Quit 1
End Sub

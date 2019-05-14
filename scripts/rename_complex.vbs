' This script was used for renaming the dataset images in order to be able to combine the Simplex and Complex datasets

Set objFso = CreateObject("Scripting.FileSystemObject")
Set Folder = objFSO.GetFolder("DIRECTORY PATH")

For Each File In Folder.Files
    sNewFile = File.Name
    sNewFile = Replace(sNewFile,".JPG",".jpg")
    if (sNewFile<>File.Name) then
        File.Move(File.ParentFolder+"\"+sNewFile)
    end if
Next
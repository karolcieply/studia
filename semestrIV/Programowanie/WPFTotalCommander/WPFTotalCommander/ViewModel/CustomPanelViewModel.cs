using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.ObjectModel;
using System.Collections.Generic;
using WPFTotalCommander.Model;
using System.ComponentModel;
using System.Windows.Input;
using System.IO;


namespace WPFTotalCommander.ViewModel
{
    internal class CustomPanelViewModel : ViewModel
    {
        public ObservableCollection<string> driveList { get; set; }
        public ObservableCollection<string> filesList { get; set; }
        public Model.Model model = null;
        private ICommand driveListClick = null;
        private ICommand changeFolder = null;
        private string currentDrive;
        private string currentPath;
        private string currentFile;
        private string errorDescription;
 
       
        public CustomPanelViewModel()
        {
            driveList = new ObservableCollection<string>();
            filesList = new ObservableCollection<string>();
            model = new Model.Model();
        }

        public ICommand DriveListClick => driveListClick ?? (driveListClick = new CommandRelay(
            o =>
            {
                List<string> drives = model.getListOfDrives();
                driveList.Clear();
                foreach(string drive in drives)
                {
                    driveList.Add(drive);
                }
            },
            null));


        public ICommand ChangeFolder => changeFolder ?? (changeFolder = new CommandRelay(
            o => CurrentPath = model.changePath(CurrentFile), 
            o => CurrentFile != null));

        public string ErrorDescription
        {
            get => errorDescription;
            set
            {
                errorDescription = value;
                onPropertyChange(nameof(ErrorDescription));
            }
        }

        public string CurrentPath
        {
            get => currentPath;
            set
            {
                currentPath = value;
                model.currentPath = currentPath;
                List<string> files = new List<string>();
                try
                {
                    files = model.getListOfPathElements();
                }
                catch
                {
                    CurrentPath = Path.GetDirectoryName(currentPath);
                    ErrorDescription = "Access eror";
                }

                if(files.Count() > 0)
                {
                    filesList.Clear();
                    foreach(string file in files)
                    {
                        filesList.Add(file);
                    }
                }

                onPropertyChange(nameof(CurrentPath));
            }
        }

        public string CurrentDrive
        {
            get => currentDrive;
            set
            {
                ErrorDescription = "";
                currentDrive = value;
                CurrentPath = CurrentDrive;
                onPropertyChange(nameof(CurrentDrive));

            }
        }

        public string CurrentFile
        {
            get => currentFile; 
            set
            {
                currentFile = value;
                ErrorDescription = "";
                onPropertyChange(nameof(CurrentFile));
            }
        }


    }
}

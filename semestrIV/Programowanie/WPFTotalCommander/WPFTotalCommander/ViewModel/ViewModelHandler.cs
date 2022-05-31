using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WPFTotalCommander.Model;
using System.ComponentModel;
using System.Windows.Input;
using System.IO;

namespace WPFTotalCommander.ViewModel
{
     class ViewModelHandler : ViewModel
    {
        private ICommand copy;
        public CustomPanelViewModel LeftPanel { get; set; }
        public CustomPanelViewModel RightPanel { get; set; }

        public ViewModelHandler()
        {
            LeftPanel = new CustomPanelViewModel();
            LeftPanel.CurrentPath = null;
            RightPanel = new CustomPanelViewModel();
            RightPanel.CurrentPath = null;
        }

        public ICommand Copy => copy ?? (copy = new CommandRelay(
            o =>
            {
                if (LeftPanel.CurrentFile == null)
                {
                    string file = RightPanel.CurrentPath + RightPanel.CurrentFile;
                    string destination = LeftPanel.CurrentPath + RightPanel.CurrentFile;
                    try
                    {
                        Copying.copyFile(file, destination);
                    }
                    catch (IOException)
                    {
                        RightPanel.ErrorDescription = "Taki plik już istnieje";
                    }
                    LeftPanel.CurrentPath = LeftPanel.CurrentPath;
                }
                else
                {
                    string file = LeftPanel.CurrentPath + LeftPanel.CurrentFile;
                    string destination = RightPanel.CurrentPath + LeftPanel.CurrentFile;
                    try
                    {
                        Copying.copyFile(file, destination);
                        
                    }
                    catch (IOException)
                    {
                        RightPanel.ErrorDescription = "Taki plik już istnieje";
                    }
                    RightPanel.CurrentPath = RightPanel.CurrentPath;

                }
            },
            o => LeftPanel.CurrentFile != null && RightPanel.CurrentPath != null || RightPanel.CurrentFile != null && LeftPanel.CurrentPath != null
            ));
    }
}

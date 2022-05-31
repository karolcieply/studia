using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace WPFTotalCommander.Model
{
     class Model
    {
        private List<string> drives;
        private List<string> pathElements = new List<string>();
        public string currentPath { get; set; }

        public List<string> getListOfDrives()
        {
            drives = new List<string>(Directory.GetLogicalDrives());
            return drives;
        }

        //stworzenie listy elementów znajdujących się pod dana ścieżką
        public List<string> getListOfPathElements()
        {
            if(currentPath != null)
            {
                pathElements.Clear();
                string[] directories = Directory.GetDirectories(currentPath);
                string[] files = Directory.GetFiles(currentPath);

                if(currentPath.Count(f => f == '\\') != 1)
                {
                    pathElements.Add("..");
                }

                foreach(string directory in directories)
                {
                    pathElements.Add("/" + Path.GetFileName(directory));
                }

                foreach (string file in files)
                {
                    pathElements.Add(Path.GetFileName(file));
                }
            }
            return pathElements;
        }

        //zmiana sciezki po wyborze
        public string changePath(string path)
        {
            if(path == "..")
            {
                currentPath = Path.GetDirectoryName(Path.GetDirectoryName(currentPath));
                if(currentPath.Last() != '\\')
                {
                    currentPath += "\\";
                }
            }
            else if (!path.StartsWith("/"))
            {
                return currentPath;
            }
            else
            {
                path = path.Remove(0, 1);
                currentPath += path;
                currentPath += "\\";
            }
            return currentPath;
        }
    }
}

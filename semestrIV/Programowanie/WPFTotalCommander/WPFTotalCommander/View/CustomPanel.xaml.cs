﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Collections.ObjectModel;

namespace WPFTotalCommander.View
{
    /// <summary>
    /// Logika interakcji dla klasy PanelTC.xaml
    /// </summary>
    public partial class CustomPanel : UserControl
    {
        public CustomPanel()
        {
            InitializeComponent();
        }

        // TextBlock
        public string PathText
        {
            get { return (string)GetValue(PathTextProperty); }
            set { SetValue(PathTextProperty, value); }
        }

        public static readonly DependencyProperty PathTextProperty = DependencyProperty.Register(
            nameof(PathText),
            typeof(string),
            typeof(CustomPanel));


        // ComboBox
        public ObservableCollection<string> DriveList
        {
            get { return (ObservableCollection<string>)GetValue(DriveListProperty); }
            set { SetValue(DriveListProperty, value); }
        }

        public static readonly DependencyProperty DriveListProperty = DependencyProperty.Register(
            nameof(DriveList),
            typeof(ObservableCollection<string>),
            typeof(CustomPanel));

        public string SelectedDrive
        {
            get { return (string)GetValue(SelectedDriveProperty); }
            set { SetValue(SelectedDriveProperty, value); }
        }

        public static readonly DependencyProperty SelectedDriveProperty = DependencyProperty.Register(
            nameof (SelectedDrive),
            typeof(string),
            typeof (CustomPanel));



        // ListBox
        public ObservableCollection<string> FilesList
        {
            get { return (ObservableCollection<string>)GetValue(FilesListProperty); }
            set { SetValue(FilesListProperty, value); }
        }

        public static readonly DependencyProperty FilesListProperty = DependencyProperty.Register(
            nameof (FilesList),
            typeof (ObservableCollection<string>),
            typeof (CustomPanel));
         
        public string SelectedFile
        {
            get { return (string)GetValue(SelectedFileProperty); }
            set { SetValue(SelectedFileProperty, value); }
        }

        public static readonly DependencyProperty SelectedFileProperty = DependencyProperty.Register(
            nameof(SelectedFile),
            typeof(string),
            typeof(CustomPanel));
          
        
        // ACTIONS / EVENTS

        // ComboBox Click
        public event RoutedEventHandler ComboboxClick
        {
            add { AddHandler(ComboboxClickEvent, value); }
            remove { RemoveHandler(ComboboxClickEvent, value); }
        }

        public static readonly RoutedEvent ComboboxClickEvent = EventManager.RegisterRoutedEvent(
            nameof(ComboboxClick),
            RoutingStrategy.Bubble,
            typeof(RoutedEventHandler),
            typeof(CustomPanel));


        public void RaiseComboboxClick()
        {
            RoutedEventArgs newEventArgs = new RoutedEventArgs(CustomPanel.ComboboxClickEvent);
            RaiseEvent(newEventArgs);
        }


        // ListBox DoubleClick
        public event RoutedEventHandler ListboxDoubleClick
        {
            add { AddHandler(ListboxDoubleClickEvent, value); }
            remove { RemoveHandler(ListboxDoubleClickEvent, value); }
        }

        public static readonly RoutedEvent ListboxDoubleClickEvent = EventManager.RegisterRoutedEvent(
            nameof(ListboxDoubleClick),
            RoutingStrategy.Bubble,
            typeof(RoutedEventHandler),
            typeof (CustomPanel));

        public void RaiseListboxDoubleClick()
        {
            RoutedEventArgs newEventArgs = new RoutedEventArgs(CustomPanel.ListboxDoubleClickEvent);
            RaiseEvent(newEventArgs);
        }


        //


        private void comboboxDropDownOpened(object sender, EventArgs e)
        {
            RaiseComboboxClick();
        }

        private void listboxMouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            RaiseListboxDoubleClick();
        }

    }



}

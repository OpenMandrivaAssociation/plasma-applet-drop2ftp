%define		oname  drop2ftp
Summary:	Copy files to a FTP server or an folder on your PC
Name:		plasma-applet-%oname
Version: 	0.6
Release: 	%mkrel 1
Source0:	97281-%oname-%version.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://kde-look.org/content/show.php/Drop2FTP?content=97281
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel

%description 
This is a KDE 4 plasma applet which can copy files with every protocol
which is supported by KIO. So you can use it to copy files to a FTP
server or an folder on your PC for example. After you have had specified
the destination in the settings of this app, you can click on the icon
to open the open-file-dialog or you can just drag and drop your files
on it.
Now you can access your personal bookmarks to use the saved addresses
Added the ability to change the Icon
Added option "Hide progress info"
If Drop2FTP is copying anything it will show it, even if there are more 
than one job

%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_applet_drop2ftp.so
%{_kde_datadir}/kde4/services/plasma-applet-drop2ftp.desktop


%prep
%setup -q -n %oname-%version


%build
%cmake_kde4
%make


%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -


%clean
rm -rf %{buildroot}


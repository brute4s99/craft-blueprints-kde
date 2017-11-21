import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = 'git://anongit.kde.org/yakuake'
        self.description = "a drop-down terminal emulator based on KDE Konsole technology"
        self.defaultTarget = 'master'

    def setDependencies(self):
        self.runtimeDependencies['kdeapps/konsole'] = 'default'


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

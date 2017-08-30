import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "Identity Management library"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["frameworks/tier3/ktextwidgets"] = "default"
        self.runtimeDependencies["frameworks/tier3/kxmlgui"] = "default"
        self.runtimeDependencies["frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcodecs"] = "default"
        self.runtimeDependencies["frameworks/tier3/kiconthemes"] = "default"
        self.runtimeDependencies["frameworks/tier3/kio"] = "default"
        self.runtimeDependencies["kde/pim/kpimtextedit"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class InjaConan(ConanFile):
    name = "inja"
    version = "2.1.0"
    url = "https://github.com/yasamoka/conan-inja"
    description = "Template engine for modern C++, loosely inspired by jinja for Python"
    license = "https://github.com/pantor/inja/blob/master/LICENSE"
    no_copy_source = True
    build_policy = "always"
    requires = "jsonformoderncpp/3.7.3@vthiery/stable"

    def source(self):
        source_url = "https://github.com/pantor/inja"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="LICENSE")
        self.copy(pattern="*.[i|h]pp", dst="include/inja", src="sources/include/inja", keep_path=True)
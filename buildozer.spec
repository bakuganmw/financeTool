[app]
# (str) Title of your application
title = Finance tool

# (str) Package name
package.name = expensemanager

# (str) Package domain (needed for android/ios packaging)
package.domain = org.beeware

# (str) Source code where the main.py lives
source.dir = .

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_patterns =

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version_regex = __version__ = ['"](.*)['"]
# version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = python3,kivy
requirements = python3,toga

# (str) Custom source folders for requirements
# Sets custom source folders for requirements
# e.g. customsource.folders = /path/to/folder1,/path/to/folder2
#customsource.folders =

# (str) Presplash of the application
#presplash.filename =

# (str) Icon of the application
#icon.filename =

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Path to the certificate to use for signing the debug version
#sign.debug.key =

# (str) The data file to use for signing the debug version
#sign.debug.data =

# (str) Path to the certificate to use for signing the release version
#sign.release.key =

# (str) The data file to use for signing the release version
#sign.release.data =

# (str) API key for an external service
#api.key =

# (str) The web key for signing REST requests
#api.rest.key =


[buildozer]
# (str) Directory in which buildozer will store its data (absolute path)
#buildozer_folder =

# (int) Number of times to retry after a failure
#buildozer_retry = 3

# (int) Number of parallel tasks buildozer will use
#buildozer_jobs = 1

# (bool) Copy the source directory to the target platform directory
# before building
# copy_source = true

# (bool) Run 'buildozer clean' at the end of the build process
# clean_at_end = false

# (bool) Enable log level (one of info, debug, warning, error, notset)
#log_level = info

# (str) Path to build logs
#log_dir =

# (str) Path to buildozer log file
#log_file =


[appdata]
# (str) Path to the application data directory (absolute path)
#appdata_dir =

# (str) Path to the application icon file (absolute path)
#appdata_icon =

# (str) Path to the application splash screen file (absolute path)
#appdata_splash =

# (str) Path to the application splash screen rotation file (absolute path)
#appdata_splash_rotate =


[distutils]
# (bool) Will install distutils (by default true)
#install = true

# (str) The pip requirements (e.g. git+, https://github.com/test/test/tarball/master)
#pip_requirements =

# (bool) Allow distutils to run with sudo privileges
#allow_sudo = false

# (bool) Include test suite
#test_suite = false


[requirements]
# (list) Application requirements
requirements = python3,toga

# (str) Custom source folders for requirements
#customsource.folders =

# (list) requirements that will be added in the source code during the packaging process
#source.include_exts = py,png,jpg,kv,atlas

# (list) Requirements that will be excluded in the source code during the packaging process
#source.exclude_exts = spec

# (list) List of requirements to be added in the source code during the packaging process
#source.include_patterns =

# (list) List of requirements to be excluded in the source code during the packaging process
#source.exclude_patterns = license,images/*/*.jpg


[android]
# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android NDK version to use (if empty, it will be automatically picked)
#android.ndk_version =

# (bool) Use only a specific Android API level (requires --allow-api-level as build parameter)
#android.api =

# (bool) Use a specific Android Build Tools version (requires --allow-build-tools-version as build parameter)
#android.build_tools_version =

# (list) Application permissions
#android.permissions = INTERNET

# (int) Android API level to target (will build against the most recent API available if not set)
#android.api = 28

# (str) Android entry point, default is ok
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the java class that implements PythonService
#android.service = org.kivy.android.PythonService

# (str) Android package domain (needed for android packaging)
#android.package_domain = org.kivy

# (str) Android package name (needed for android packaging)
#android.package_name =

# (str) Android application name (needed for android packaging)
#android.application_name =

# (str) Android package version (needed for android packaging)
#android.package_version = 0.1

# (str) Android package license (needed for android packaging)
#android.package_license =

# (str) Android package license (needed for android packaging)
#android.package_license =

# (str) Presplash of the application
#presplash.filename =

# (str) Icon of the application
#icon.filename =

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
#orientation = all

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Path to the certificate to use for signing the debug version
#sign.debug.key =

# (str) The data file to use for signing the debug version
#sign.debug.data =

# (str) Path to the certificate to use for signing the release version
#sign.release.key =

# (str) The data file to use for signing the release version
#sign.release.data =

# (str) API key for an external service
#api.key =

# (str) The web key for signing REST requests
#api.rest.key =


[web]
# (str) URL for the API of the web service
#api.url =

# (str) URL for the web service
#web.url =

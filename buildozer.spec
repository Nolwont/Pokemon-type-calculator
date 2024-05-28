title = Pokemon Type Calculator
package.name = pokemontypecalc

package.domain = org.test
source.dir = .

source.include_exts = py,png,jpg,kv,atlas,data,ep,ico
p4a.branch = release-2022.12.20

version = 0.1

requirements = python3==3.7.6,hostpython3==3.7.6,cython==0.29.33,kivy,kivymd==1.1.1,pillow

presplash.filename = %(source.dir)s/data/presplash.jpg
icon.filename = %(source.dir)s/data/icon.ico

orientation = portrait

osx.python_version = 3.7.6
osx.kivy_version = 1.9.1

fullscreen = 1

android.permissions = android.permission.INTERNET,android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE

dump=eestec_db
dump_path=install/dump/$dump

export DJANGO_SETTINGS_MODULE=eestec_site.settings
cp $dump_path .
./manage.py syncdb
./parse.py

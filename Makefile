all:

clean:

install:
	chmod 755 banner.py
	chmod 755 install.py
	chmod 755 run.sh
	chmod 755 dev-x-hack-scanerer.py
	mkdir -p $(DESTDIR)/opt/dev-x-hack-scanerer/
	mkdir -p $(DESTDIR)/usr/share/doc/dev-x-hack-scanerer/
	mkdir -p $(DESTDIR)/opt/dev-x-hack-scanerer/tools/
	mkdir -p $(DESTDIR)/usr/bin/
	cp banner.py $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp install.py $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp LICENSE $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp Makefile $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp README.md $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp README.md $(DESTDIR)/usr/share/doc/dev-x-hack-scanerer/
	cp run.sh $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp run.sh $(DESTDIR)/usr/bin/
	cp dev-x-hack-scanerer.py $(DESTDIR)/opt/dev-x-hack-scanerer/
	cp -r tools $(DESTDIR)/opt/dev-x-hack-scanerer/
	


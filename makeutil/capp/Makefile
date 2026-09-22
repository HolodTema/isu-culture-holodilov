# .PHONY says to make, that these targets are not filenames, they are just names of some targets
# so, if someone could create, for example, file with name 'app', target 'app' will 
# be broken because of make suppose that build-target is file with name build
#
# for example, we launch make app
# file app will be created 
# and then we launch make app again
# and the second time the target will not be launched, because we already have app file,
# and 'app' target is not in PHONY
#
# rule for Makefiles: all the targets which are not output-files-names we put to .PHONY
.PHONY: another-app

build: main.c
	gcc main.c -o app

app: main.c
	gcc main.c -o app

another-app: main.c
	gcc main.c -o another-app


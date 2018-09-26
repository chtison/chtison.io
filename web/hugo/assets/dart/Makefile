.PHONY: all clean re

FILES := main
FILES := $(addsuffix .dart, $(FILES))
OUT   := $(addprefix ../, $(addsuffix .js, $(FILES)))

all: $(OUT)

../%.dart.js: %.dart
	dart2js $< -o $@ -m --no-source-maps --fatal-warnings
	rm -f -- $@.deps

clean:
	rm -f -- $(OUT)

re: clean all

JOURNAL=journal.html journal.odt
ALL=$(JOURNAL)

.PHONY: all
all: $(ALL)

.PHONY: journal
journal: $(JOURNAL)

.PHONY: pdfs
pdfs: $(PDF)

journal.html: journal.md
	pandoc -s $^ -o $@

journal.odt: journal.md
	pandoc $^ -o $@

.PHONY: tidy
tidy: journal.md
	tidy-markdown < journal.md | sponge journal.md

.PHONY: count
count: journal.md count_time_spent.py
	python count_time_spent.py journal.md

.PHONY: clean
clean:
	rm -f $(ALL)

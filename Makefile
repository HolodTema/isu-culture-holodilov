.DEFAULT_GOAL := help

create-practice:
ifndef PRACTICE:
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)

remove-practice:
ifndef PRACTICE:
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)

help:
	@echo "This Makefile is for repo-level activity to create subrepositories"


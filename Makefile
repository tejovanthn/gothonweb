NAME = ${notdir ${CURDIR}}

BIN  = bin
PRJ  = $(NAME)
TST  = tests

add: clean
	@git add .
	@git status

clean:
	@rm -rf $(BIN)/*.pyc
	@rm -rf $(PRJ)/*.pyc
	@rm -rf $(TST)/*.pyc

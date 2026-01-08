CREATE OR ALTER PROCEDURE ver_extrato
    @p_cliente_id UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @saldo_atual INT;

	-- Obtém saldo atual do cliente
	SELECT @saldo_atual = saldo
	FROM clients
	WHERE id = @p_cliente_id

	-- Mostra saldo atual
	PRINT 'Saldo atual do cliente: ' + CAST(@saldo_atual as VARCHAR(20));

	-- Retorna as 10 ultimas transações do cliente
	SELECT TOP 10
		id,
		tipo,
		descricao,
		valor,
		realizada_em
	FROM transactions
	WHERE cliente_id = @p_cliente_id
	ORDER BY realizada_em DESC
END;
GO
CREATE OR ALTER PROCEDURE realizar_transacao
    @p_tipo CHAR(1),
    @p_descricao VARCHAR(10),
    @p_valor INT,
    @p_cliente_id UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @saldo_atual INT;
    DECLARE @limite_cliente INT;
    DECLARE @saldo_apos_transacao INT;

    -- Buscar saldo e limite do cliente
    SELECT @saldo_atual = saldo, @limite_cliente = limite
    FROM clients
    WHERE id = @p_cliente_id;

    PRINT 'Saldo atual do cliente: ' + CAST(@saldo_atual AS VARCHAR(20));
    PRINT 'Limite atual do cliente: ' + CAST(@limite_cliente AS VARCHAR(20));

    -- Verificar limite
    IF @p_tipo = 'd' AND @saldo_atual - @p_valor < -@limite_cliente
    BEGIN
        RAISERROR('Limite inferior ao necessário para a transação', 16, 1);
        RETURN;
    END;

    -- Atualizar saldo
    UPDATE clients
    SET saldo = saldo + CASE WHEN @p_tipo = 'd' THEN -@p_valor ELSE @p_valor END
    WHERE id = @p_cliente_id;

    -- Registrar transação
    INSERT INTO transactions (tipo, descricao, valor, cliente_id)
    VALUES (@p_tipo, @p_descricao, @p_valor, @p_cliente_id);

    -- Mostrar saldo após transação
    SELECT @saldo_apos_transacao = saldo
    FROM clients
    WHERE id = @p_cliente_id;

    PRINT 'Saldo cliente após transação: ' + CAST(@saldo_apos_transacao AS VARCHAR(20));
END;
GO

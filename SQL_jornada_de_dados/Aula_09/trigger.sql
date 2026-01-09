CREATE TRIGGER trg_salario_modificado
ON Funcionario
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Insere na tabela de auditoria apenas quando o salário for alterado
    IF UPDATE(salario)
    BEGIN
        INSERT INTO Funcionario_Auditoria (id, salario_antigo, novo_salario, data_de_modificacao_do_salario)
        SELECT 
            d.id,
            d.salario,   -- valor antigo
            i.salario,   -- novo valor
            GETDATE()
        FROM deleted d
        INNER JOIN inserted i ON d.id = i.id;
    END
END;
GO

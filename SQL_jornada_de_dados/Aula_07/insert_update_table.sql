-- Inserir dados na tabela clients
INSERT INTO clients (limite, saldo)
VALUES
    (100000, 0),
    (80000, 0),
    (1000000, 0),
    (10000000, 0),
    (500000, 0);

-- Inserir transação
INSERT INTO transactions (tipo, descricao, valor, cliente_id)
VALUES ('d', 'Carro', 80000, '4B89364C-A2EC-4360-BDEC-362281E1584C'),

UPDATE clients
SET saldo = saldo + CASE WHEN 'd' = 'd' THEN -80000 ELSE 80000 END
WHERE id = '4B89364C-A2EC-4360-BDEC-362281E1584C';

select * from clients
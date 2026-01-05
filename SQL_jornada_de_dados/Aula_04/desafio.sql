-- Faça a classificação dos produtos mais venvidos usando usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- Essa questão tem 2 implementações, veja uma que utiliza subquery e uma que não utiliza.
-- Tabelas utilizadasFROM order_details o JOIN products p ON p.product_id = o.product_id;
SELECT  
  o.OrderID, 
  p.ProductName, 
  (o.UnitPrice * o.Quantity) AS total_sale,
  ROW_NUMBER() OVER (ORDER BY (o.UnitPrice * o.Quantity) DESC) AS order_rn, 
  RANK() OVER (ORDER BY (o.UnitPrice * o.Quantity) DESC) AS order_rank, 
  DENSE_RANK() OVER (ORDER BY (o.UnitPrice * o.Quantity) DESC) AS order_dense
FROM  
  [Order Details] o
JOIN 
  Products p ON p.ProductID = o.ProductID;

SELECT  
  sales.ProductName, 
  total_sale,
  ROW_NUMBER() OVER (ORDER BY total_sale DESC) AS order_rn, 
  RANK() OVER (ORDER BY total_sale DESC) AS order_rank, 
  DENSE_RANK() OVER (ORDER BY total_sale DESC) AS order_dense
FROM (
  SELECT 
    p.ProductName, 
    SUM(o.UnitPrice * o.Quantity) AS total_sale
  FROM  
    [Order Details] o
  JOIN 
    Products p ON p.ProductID = o.ProductID
  GROUP BY p.ProductName
) AS sales
ORDER BY sales.ProductName;

-- Listar funcionários dividindo-os em 3 grupos usando NTILE
-- FROM employees;
SELECT EmployeeID, 
	FirstName, 
	LastName, 
	NTILE(3) OVER (ORDER BY EmployeeID) AS grupo 
FROM Employees;

-- Ordenando os custos de envio pagos pelos clientes de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
-- FROM orders JOIN shippers ON shippers.shipper_id = orders.ship_via;
SELECT 
    o.OrderID,
    o.CustomerID,
    s.CompanyName AS Shipper,
    o.OrderDate,
    o.Freight AS ShippingCost,
    LAG(o.Freight, 1) OVER (ORDER BY o.OrderDate) AS PreviousCost,
    LEAD(o.Freight, 1) OVER (ORDER BY o.OrderDate) AS NextCost
FROM Orders o
JOIN Shippers s 
    ON s.ShipperID = o.ShipVia
ORDER BY o.OrderDate;


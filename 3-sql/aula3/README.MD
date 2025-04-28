# Aula 03 -  SQL para Analytics: Join and Having in SQL

Introdução aos Joins em SQL
Joins em SQL são fundamentais para combinar registros de duas ou mais tabelas em um banco de dados com base em uma condição comum, geralmente uma chave estrangeira. Essa técnica permite que dados relacionados, que são armazenados em tabelas separadas, sejam consultados juntos de forma eficiente e coerente.

Os joins são essenciais para consultar dados complexos e para aplicações em que a normalização do banco de dados resulta em distribuição de informações por diversas tabelas.

Existem vários tipos de joins, cada um com seu uso específico dependendo das necessidades da consulta:

Inner Join: Retorna registros que têm correspondência em ambas as tabelas.
Left Join (ou Left Outer Join): Retorna todos os registros da tabela esquerda e os registros correspondentes da tabela direita. Se não houver correspondência, os resultados da tabela direita terão valores NULL.
Right Join (ou Right Outer Join): Retorna todos os registros da tabela direita e os registros correspondentes da tabela esquerda. Se não houver correspondência, os resultados da tabela esquerda terão valores NULL.
Full Join (ou Full Outer Join): Retorna registros quando há uma correspondência em uma das tabelas. Se não houver correspondência, ainda assim, o resultado aparecerá com NULL nos campos da tabela sem correspondência.
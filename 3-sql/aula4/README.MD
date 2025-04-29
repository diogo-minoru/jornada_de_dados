# Aula 04 -  SQL para Analytics: Windows Function

As `Windows Function` permitem uma análise de dados eficiente e precisa, ao possibilitar cálculos dentro de `partições ou linhas específicas`. Elas são cruciais para tarefas como classificação, agregação e análise de tendências em consultas SQL.

Essas funções são aplicadas a cada linha de um conjunto de resultados, e utilizam uma cláusula `OVER()` para determinar como cada linha é processada dentro de uma "janela", permitindo controle sobre o comportamento da função dentro de um grupo de dados ordenados.

Window Functions Syntax componentes
```sql
window_function_name(arg1, arg2, ...) OVER (
  [PARTITION BY partition_expression, ...]
  [ORDER BY sort_expression [ASC | DESC], ...]
)
```

* **window_function_name**: Este é o nome da função de janela que você deseja usar, como SUM, RANK, LEAD, etc.

* **arg1, arg2, ...:** Estes são os argumentos que você passa para a função de janela, se ela exigir algum. Por exemplo, para a função SUM, você especificaria a coluna que deseja somar.

* **OVER**: Principal conceito das windows functions, ele que cria essa "Janela" onde fazem nossos cálculos

* **PARTITION BY:** Esta cláusula opcional divide o conjunto de resultados em partições ou grupos. A função de janela opera independentemente dentro de cada partição.

* **ORDER BY:** Esta cláusula opcional especifica a ordem em que as linhas são processadas dentro de cada partição. Você pode especificar a ordem ascendente (ASC) ou descendente (DESC).

```sql
SELECT DISTINCT order_id,
   COUNT(order_id) OVER (PARTITION BY order_id) AS unique_product,
   SUM(quantity) OVER (PARTITION BY order_id) AS total_quantity,
   SUM(unit_price * quantity) OVER (PARTITION BY order_id) AS total_price
FROM order_details
ORDER BY order_id;
```
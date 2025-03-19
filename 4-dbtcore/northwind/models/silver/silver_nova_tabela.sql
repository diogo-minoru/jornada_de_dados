with renamed as (
    select 
        id_transacao,
        id_cliente,
        data,
        valo_total as valor_total,
        parcelas,
        valor_parcela,
        taxa_juros
    from {{ref('bronze_nova_tabela')}}
)

select *
from renamed
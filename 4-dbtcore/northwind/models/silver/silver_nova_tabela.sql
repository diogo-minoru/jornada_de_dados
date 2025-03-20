with 
    source as (
    select *
    from {{ref('bronze_nova_tabela')}}
    ),

    renamed as (
    select 
        id_transacao,
        id_cliente,
        data,
        valo_total as valor_total,
        parcelas,
        valor_parcela,
        taxa_juros
    from source
    )

select *
from renamed
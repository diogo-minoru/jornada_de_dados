with renamed as (
    select 
        id_transacao,
        id_cliente,
        data,
        valo_total as valor_total,
        parcelas,
        valor_parcela,
        taxa_juros
    from {{ref('raw_crm__nova_tabela')}}
)

select *
from renamed
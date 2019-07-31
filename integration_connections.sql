with dd as
(select
  distinct date_trunc('month', date)::timestamp as date
from
  product.crm_map_connections c
where
  date >= '2018-12-01 00:00:00'),
ci as
(select
  a.org_id_c as org_id,
  a.go_live_timestamp_c as go_live_date,
  a.finance_c as segment,
  a.icp_c as is_icp,
  a.live_integrations_c as live_integrations
from
  salesforce.accounts a
where
  a.org_id_c is not null
  and a.org_id_c != ''
  and a.is_deleted != true
  and a.live_integrations_c like '%salesforce%'),
tmp as
(select
  c.date,
  c.org_id as org_id,
  ci.live_integrations as live_int,
  ci.is_icp,
  case when (ci.go_live_date > c.date or ci.go_live_date is null) then 'not live'
    when (ci.go_live_date <= d.date) then 'live'
    end as live_ind,
  case when (ci.live_integrations like '%salesforce%') then 1
    when (ci.live_integrations not like '%salesforce%') then 0
    end as sf_ind
from
  product.crm_map_connections c
join dd on c.date = dd.date
join ci on c.org_id = ci.org_id
where
  c.is_icp = true
  and mrr > 0
  and dd.date is not null
group by 1, 2, 3, ci.go_live_date, ci.is_icp),
calc as
(select
  date_part('year', date) as year,
  date_part('month', date) as month,
  live_ind,
  cast(count(distinct org_id) as float) as icp_orgs
  cast(sum(sf_ind) as float) as sf_connected_orgs
from
  tmp
where
  is_icp = 'ICP'
group by 1, 2, 3);

select
  year || '-' || lpad(month::text,2,'0') as yr_month,
  year,
  sf_connected,
  icp_orgs - sf_connected as not_sf_connected,
  live_ind
from
  calc;

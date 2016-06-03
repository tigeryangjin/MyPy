select (case
         when store_close_date is not null then
          '--已闭店' || '【' || key_value_1 || store_name || '】' || '--'
         else
          ''
       end) || 'connect ' || (case
         when instr(key_value_1, '13') = 1 then
          'bbgdq'
         when instr(key_value_1, '120072') = 1 then
          'bbgdq'
         when instr(key_value_1, '120040') = 1 then
          'bbgdq'
         else
          'bbgcs'
       end) || '/drowssap@' || key_value_1 || chr(10) || (case
         when store_close_date is not null then
          '--'
         else
          ''
       end) || '@ D:\bbgcs\' || 'tb' || '.sql' || chr(10) text,
       a.key_value_1,
       store_name,
       a.state,
       description,
       store_format,
       row_number() over(partition by a.state, store_format order by a.state, key_value_1) pm
  from addr a, State b, store c
 where a.state = b.State
   and a.key_value_1 = c.store
   and key_value_1 < '140000'
   and addr_type in (01)
   and module = 'ST' --and b.state in (43) 
 order by a.state, store_format, key_value_1

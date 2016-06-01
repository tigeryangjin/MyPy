select text
  from (select text, trunc(pm / 10) + 1 pm
          from (select 'copy from ' || (case
                         when instr(key_value_1, '13') = 1 then
                          'bbgdq'
                         when instr(key_value_1, '120072') = 1 then
                          'bbgdq'
                         when instr(key_value_1, '120040') = 1 then
                          'bbgdq'
                         else
                          'bbgcs'
                       end) || '/drowssap@' || key_value_1 || chr(32) || 'to' ||
                       chr(32) || 'bbgcs/drowssap@XL120017N159' || chr(32) ||
                       'INSERT' || chr(32) || 'dpm001' || chr(32) ||
                       'using select * from dpm' || chr(59) || chr(10) text,
                       a.key_value_1,
                       store_name,
                       a.state,
                       description,
                       (case
                         when store_format in (1, 2) then
                          1
                         else
                          2
                       end) store_format,
                       row_number() over(partition by store_format order by a.state, key_value_1) pm
                  from addr a, State b, store c
                 where a.state = b.State
                   and a.key_value_1 = c.store
                   and key_value_1 < '140000'
                   and addr_type in (01)
                   and module = 'ST'))

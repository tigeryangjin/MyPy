set line1000 pause off head OFF pagesize 0 trims on;
spool D:\bbgcs\log\hn1.log

connect bbgcs/drowssap@120001
@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120002
@ D:\bbgcs\tb.sql

--已闭店【120003新华店】--connect bbgcs/drowssap@120003
--@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120004
@ D:\bbgcs\tb.sql

--已闭店【120006醴陵店】--connect bbgcs/drowssap@120006
--@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120008
@ D:\bbgcs\tb.sql

--已闭店【120009锰矿店】--connect bbgcs/drowssap@120009
--@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120010
@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120011
@ D:\bbgcs\tb.sql

--已闭店【120012桥西店】--connect bbgcs/drowssap@120012
--@ D:\bbgcs\tb.sql

--已闭店【120013购物广场超市】--connect bbgcs/drowssap@120013
--@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120014
@ D:\bbgcs\tb.sql

connect bbgcs/drowssap@120015
@ D:\bbgcs\tb.sql

spool off;
exit;
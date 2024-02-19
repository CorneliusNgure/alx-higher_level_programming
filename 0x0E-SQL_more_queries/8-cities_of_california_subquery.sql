-- Lists all California cities on the hbtn_0d_usa database.
-- in the ascend order by cities.id.

SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;

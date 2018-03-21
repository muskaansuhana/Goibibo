import pymysql

def connect_to_database(hostName,user,password,db):
	conn = 	pymysql.connect(host=hostName,user=user,password=password,db=db)
	return conn

def get_cities_with_highest_hotel_booking(crsr,limit):
	query = "SELECT city_id,count(city_id) AS frequency FROM Hotels GROUP BY city_id ORDER BY count(city_id) DESC LIMIT "+ str(limit) +";"
	crsr.execute(query)
	return crsr.fetchall()

def get_cities_with_highest_hotel_rooms_booked(crsr,limit):
	query = "SELECT city_id, SUM(rooms) AS 'total_rooms' FROM Hotels GROUP BY city_id ORDER BY total_rooms DESC LIMIT "+str(limit)+";"
	crsr.execute(query)
	return crsr.fetchall()

def get_user_who_booked_max_rooms(crsr):
	query = " SELECT user_id,SUM(rooms) AS total_rooms FROM Hotels GROUP BY user_id ORDER BY total_rooms DESC LIMIT 1"
	crsr.execute(query)
	return crsr.fetchall()

def get_max_booking_in_recent_days(crsr,days,limit): 
	query = "SELECT user_id , cnt FROM ( SELECT user_id,count(user_id) as cnt FROM Hotels where booking_date > timestampadd(year,-"+str(days)+",now() ) GROUP BY user_id ) as t ORDER BY cnt DESC LIMIT "+str(limit)+";"
	crsr.execute(query)
	return crsr.fetchall()

host_name = ""
user = ""
password = ""
db = ""

conn = connect_to_database(hostName,user,password,db)
crsr = conn.cursor()

print (get_cities_with_highest_hotel_booking(crsr,10))

print (get_cities_with_highest_hotel_rooms_booked(crsr,10))

print (get_user_who_booked_max_rooms(crsr))

print(get_max_booking_in_recent_days(crsr,30,10))

conn.close()
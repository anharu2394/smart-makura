json.partial! "users/user", user: @user
json.set_hour @user.set_at.hour
json.set_min @user.set_at.min

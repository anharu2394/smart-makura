class ChangeDatatypeSetTimeOfSleepData < ActiveRecord::Migration[5.1]
  def change
    change_column :sleep_data,:set_at,:time 
  end
end

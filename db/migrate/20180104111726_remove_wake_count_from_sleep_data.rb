class RemoveWakeCountFromSleepData < ActiveRecord::Migration[5.1]
  def change
    remove_column :sleep_data, :wake_count, :integer
  end
end

class CreateSleepData < ActiveRecord::Migration[5.1]
  def change
    create_table :sleep_data do |t|
      t.datetime :finished_at
      t.integer :wake_count
      t.datetime :set_at

      t.timestamps
    end
  end
end

class AddSetAtToUser < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :set_at, :time
  end
end

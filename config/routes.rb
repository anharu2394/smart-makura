Rails.application.routes.draw do
  resources :sleep_data
  resources :users
  root 'sleep_data#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end

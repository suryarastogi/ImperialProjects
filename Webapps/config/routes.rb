Rails.application.routes.draw do

  resources :competitors
  resources :matches
  resources :competitions
  get 'pages/home'

  resources :channels do
    resources :updates
  end
  
  resources :sports 
  resources :users
  root 'pages#home'

  resources :chats do
    resources :messages
  end
  resources :groups do
    get "addnew"
    get "removeself"
  end
  
  resources :matches do
    member do
      patch 'goal'
      patch 'game_over'
    end
  end

  get    'index'   => 'users#index',  :as => :index
  get    'signup'  => 'users#new',    :as => :signup
  get    'login'   => 'sessions#new'
  post   'login'   => 'sessions#create'
  get    'logout'  => 'sessions#destroy'
  get    'newasd'  => 'users#findex'
  #get    'leagues' => 'leagues#index'
  #get    'sports'  => 'sports#index'
  #get    'matches' => 'matches#index'
  
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end

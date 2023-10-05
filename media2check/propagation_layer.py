# Twitter API tweepy used, credential and authenticate here removed for security reasons

def get_propagation_layer(user_id, depth=1, max_depth=2):
    if depth > max_depth:
        return []
    
    followers = api.followers_ids(user_id)
    friends = api.friends_ids(user_id)
    
    propagation_layer = set(followers + friends)
    
    next_layer = []
    
    for follower_id in followers:
        next_layer.extend(get_propagation_layer(follower_id, depth + 1, max_depth))
    
    for friend_id in friends:
        next_layer.extend(get_propagation_layer(friend_id, depth + 1, max_depth))
    
    propagation_layer.update(next_layer)
    
    return list(propagation_layer)

# Placeholder 'twitter_username', input user name for analysis
username = 'twitter_username'
user = api.get_user(screen_name=username)
user_id = user.id

propagation_layer = get_propagation_layer(user_id, max_depth=2)

print(f"Propagation Layer for {username}:")
for i, user_id in enumerate(propagation_layer, 1):
    user = api.get_user(id=user_id)
    print(f"{i}. {user.screen_name}")

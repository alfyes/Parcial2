require 'calabash-android/calabash_steps'

When /^take screenshot with name "(\w+)"$/ do |name|
    screenshot_embed(name:name)
end
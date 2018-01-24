require 'test_helper'

class SleepDataControllerTest < ActionDispatch::IntegrationTest
  setup do
    @sleep_datum = sleep_data(:one)
  end

  test "should get index" do
    get sleep_data_url
    assert_response :success
  end

  test "should get new" do
    get new_sleep_datum_url
    assert_response :success
  end

  test "should create sleep_datum" do
    assert_difference('SleepDatum.count') do
      post sleep_data_url, params: { sleep_datum: { finished_at: @sleep_datum.finished_at, set_at: @sleep_datum.set_at, wake_count: @sleep_datum.wake_count } }
    end

    assert_redirected_to sleep_datum_url(SleepDatum.last)
  end

  test "should show sleep_datum" do
    get sleep_datum_url(@sleep_datum)
    assert_response :success
  end

  test "should get edit" do
    get edit_sleep_datum_url(@sleep_datum)
    assert_response :success
  end

  test "should update sleep_datum" do
    patch sleep_datum_url(@sleep_datum), params: { sleep_datum: { finished_at: @sleep_datum.finished_at, set_at: @sleep_datum.set_at, wake_count: @sleep_datum.wake_count } }
    assert_redirected_to sleep_datum_url(@sleep_datum)
  end

  test "should destroy sleep_datum" do
    assert_difference('SleepDatum.count', -1) do
      delete sleep_datum_url(@sleep_datum)
    end

    assert_redirected_to sleep_data_url
  end
end

class SleepDataController < ApplicationController
  before_action :set_sleep_datum, only: [:show, :edit, :update, :destroy]

  # GET /sleep_data
  # GET /sleep_data.json
  def index
    @sleep_data = SleepDatum.order("finished_at DESC").all
    @set_at = User.find(1).set_at.strftime("%H時%M分")
  end

  # GET /sleep_data/1
  # GET /sleep_data/1.json
  def show
  end

  # GET /sleep_data/new
  def new
    @sleep_datum = SleepDatum.new
  end

  # GET /sleep_data/1/edit
  def edit
  end

  # POST /sleep_data
  # POST /sleep_data.json
  def create
    @sleep_datum = SleepDatum.new(sleep_datum_params)

    respond_to do |format|
      if @sleep_datum.save
        format.html { redirect_to @sleep_datum, notice: 'Sleep datum was successfully created.' }
        format.json { render :show, status: :created, location: @sleep_datum }
      else
        format.html { render :new }
        format.json { render json: @sleep_datum.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /sleep_data/1
  # PATCH/PUT /sleep_data/1.json
  def update
    respond_to do |format|
      if @sleep_datum.update(sleep_datum_params)
        format.html { redirect_to @sleep_datum, notice: 'Sleep datum was successfully updated.' }
        format.json { render :show, status: :ok, location: @sleep_datum }
      else
        format.html { render :edit }
        format.json { render json: @sleep_datum.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /sleep_data/1
  # DELETE /sleep_data/1.json
  def destroy
    @sleep_datum.destroy
    respond_to do |format|
      format.html { redirect_to sleep_data_url, notice: 'Sleep datum was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_sleep_datum
      @sleep_datum = SleepDatum.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def sleep_datum_params
      params.require(:sleep_datum).permit(:finished_at,  :set_at)
    end
end

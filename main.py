from pathlib import Path

from twiggy import quick_setup, log

from build_model import BuildModel
from captcha_type_recognizer import captcha_type_recognizer
from check_model_accuracy import CheckModelAccuracy
from prepare_data import PrepareData
from train_model import TrainModel

quick_setup()  # Set basic logging functions from Twiggy

def main():
    log.info(f' {"-" * 10} Starting ... {"-" * 10} ')
    # Set True to update captcha type recognizer model
    update_captcha_recognizer: bool = True

    if update_captcha_recognizer:
        log.info(f' {"-" * 10} Captcha Type Recognizer model WILL be updated. {"-" * 10} ')
        captcha_type_recognizer.train_recognizer_model()

    # Name of data set to train
    captcha_set_to_train: str = 'captcha_type_b'
    # Image format
    image_format: str = 'jpeg'
    # Path to the data set to train
    data_dir: Path = Path(f'C:\Users\Suraj\Desktop\Suraj_Proplegit\captcha_solving_ocr\captcha_data_sets\{captcha_set_to_train}')

    # Get prepared data
    prepared_data = PrepareData(data_dir, image_format, captcha_set_to_train)

    # Show training data set
    prepared_data.show_train_data_set()

    # Get model
    model = BuildModel(prepared_data)
    model = model.build_model()
    model.summary()

    # Train Model
    trained_model = TrainModel(prepared_data).train_model(model)

    # Show Model Accuracy
    CheckModelAccuracy(prepared_data).show_validation_dataset(trained_model)

    log.info(f' {"-" * 10} DONE! {"-" * 10} ')


if __name__ == '__main__':
    main()

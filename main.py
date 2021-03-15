
import ConnectFour_GUI as cfg
import ConnectFour_model as cfm

def main():
    model = cfm.ConnectFour_model()
    cfg.ConnectFour_GUI(model)

if __name__ == "__main__":
    main()
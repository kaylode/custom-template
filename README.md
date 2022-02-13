# <p align="center"> :ship: Ship of Theseus :ship: </p>

> The ship wherein Theseus and the youth of Athens returned from Crete had thirty oars, and was preserved by the Athenians down even to the time of Demetrius Phalereus, for they took away the old planks as they decayed, putting in new and stronger timber in their places, insomuch that this ship became a standing example among the philosophers, for the logical question of things that grow; one side holding that the ship remained the same, and the other contending that it was not the same.
> — Plutarch, Theseus

-------------------------------------------------------
<details close> <summary><strong>Dev logs</strong></summary>
 <strong><i>[10/02/2022]</i></strong> SUPER POWER NINJA TURBO NEO ULTRA HYPER MEGA MULTI ALPHA META EXTRA UBER PREFIX -REFACTOR!!!! <a href="https://github.com/kaylode/custom-template/pull/7">#7</a> <br> 
</details>

# Instructions

### To adapt for personal project
1. Create your own dataset, dataloader, model, loss function, metric function, ... and register it to the registry so that it can be generated from config at runtime.
2. Customize inherited trainer and pipeline to your need, such as what to do before/after training/validating step,...
3. Modify configuration file

*See ```torckay/classification``` for example*

### To execute scripts with arguments
- Run the script with `-c` flag with specified config file. Example:

```
python train.py -c pipeline.yaml
```

- To override arguments inside the .yaml file, use flag `-o` with key and value. For example, to train 50 epochs and resume training from checkpoints:

```
python train.py \
    -c pipeline.yaml \
    -o trainer.args.num_epochs=50 \
    global.resume=checkpoint.pth
```
**Notice: There are no spaces between keys and values in -o flag**

- Also, if you want to do inference, you need to write your own script. For example see ```configs/classification/infer.py```


# :blue_book: References
- This repo is inspired by https://github.com/vltanh/torchan <span style="color:yellow"> **Remember to give it a star** </span>.
- The big refactor is mostly adapted from https://github.com/HCMUS-ROBOTICS/ssdf-nncore 's nncore, which also deserves stars.

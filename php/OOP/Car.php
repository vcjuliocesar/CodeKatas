<?php

/**
 * @property string $color
 * @property string $uniqueId
 * @property string $doors
 * @property string $wheels
 * @property string $model
 */

interface vehicle
{

    public function start_engine();

    public function stop_engine();

    public function honk();
}

/**
 * @property string $batery
 */
interface ElectricVehicle extends vehicle
{
    public function charge();
}

class HybridCar implements vehicle
{

    public $doors;

    public $wheels;

    public $model;

    public function __construct($model,$doors = 4, $wheels = 4)
    {
        $this->doors = $doors;

        $this->wheels = $wheels;

        $this->model = $model;
    }

    public function start_engine()
    {
        return "success ".$this->model;
    }

    public function stop_engine()
    {
    }

    public function alternase()
    {
        return "alternase beetwen engine and batery";
    }

    public function honk()
    {
    }
}


class ElectricCar implements vehicle
{

    public $doors;

    public $wheels;

    public $model;


    public function __construct($doors = 4, $wheels = 4, $model)
    {
        $this->doors = $doors;

        $this->wheels = $wheels;

        $this->model = $model;
    }

    public function start_engine()
    {
        return "success";
    }

    public function stop_engine()
    {
    }

    public function batery()
    {
        return "i use batery";
    }

    public function honk()
    {
    }
}

class Car implements vehicle
{

    public $doors;

    public $wheels;

    public $model;

    public function __construct($model,$doors = 4, $wheels = 4)
    {
        $this->doors = $doors;

        $this->wheels = $wheels;

        $this->model = $model;
    }

    public function start_engine()
    {
        return "success";
    }

    public function stop_engine()
    {
    }

    public function engine()
    {
        return "i use gas";
    }

    public function honk()
    {
    }
}

class Motorcycle implements vehicle
{
    public $wheels;

    public $model;

    public function __construct($wheels = 2, $model)
    {
        $this->wheels = $wheels;
        $this->model = $model;
    }

    public function start_engine()
    {
        return "success";
    }

    public function stop_engine()
    {
    }

    public function honk()
    {
    }
}

class ElectricMotorcycle implements ElectricVehicle
{

    public function __construct($model,$doors = 4, $wheels = 4)
    {
        $this->doors = $doors;

        $this->wheels = $wheels;

        $this->model = $model;
    }

    public function charge()
    {
    }

    public function start_engine()
    {
        return "susses electric vehicle ".$this->model;
    }

    public function stop_engine()
    {
    }

    public function honk()
    {
    }
}

$prius = new HybridCar("priusA");

echo $prius->start_engine();

echo "<br>";

$mazda = new HybridCar("mazdaE");

echo $mazda->start_engine();

echo "<br>";

$bmw = new ElectricMotorcycle("bwm123");

echo  $bmw->start_engine();

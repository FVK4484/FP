package fp.consumos.test;

import java.time.LocalDate;

import fp.consumos.Consumo;
import fp.consumos.TipoEdificio;

public class TestConsumo {

	public static void main(String[] args) {
		
		Consumo consumo1 = new Consumo(LocalDate.of(2023, 12, 1), 
				"20", TipoEdificio.CENTROS_CULTURALES_BIBLIOS, 
				"Biblioteca Pío Baroja", "ACACIAS", "Gas", "Gas", 
				"m3", 807.6);
		Consumo consumo2 = new Consumo(LocalDate.of(2023, 11, 1), 
				"20", TipoEdificio.CENTROS_CULTURALES_BIBLIOS, 
				"Biblioteca Pío Baroja", "ACACIAS", "Gas", "Gas", 
				"m3", 800.6);	
		
		System.out.println(consumo1);
		System.out.println(consumo2);
		
		if (consumo1.consumo() > consumo2.consumo()) {
			
			System.out.println("El mes " + consumo1.fecha().getMonthValue() + " ha habido mayor consumo.");
	
		}
		
		else {
			
			System.out.println("El mes " + consumo2.fecha().getMonthValue() + " ha habido mayor consumo.");
			
		}
		
	}

}

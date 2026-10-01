package fp.consumos.test;

import java.util.List;

import fp.consumos.Consumo;
import fp.consumos.EstadisticasConsumo;
import fp.consumos.FactoriaConsumos;

public class TestEstadisticasConsumo {

	public static void main(String[] args) {
		
		List<Consumo> consumos = FactoriaConsumos.leeConsumos("./data/consumo_energia_edificios.csv");
		
		EstadisticasConsumo estadisticas = new EstadisticasConsumo(consumos);

        System.out.println("---- PREGUNTA 1: TOP BARRIOS (2020) ----");
        System.out.println("Top 3 Barrios (GAS): " + 
        		estadisticas.getBarriosTopConsumo(2020, "Gas", 3));
        System.out.println("Top 3 Barrios (ENERGIA ACTIVA): " + 
                estadisticas.getBarriosTopConsumo(2020, "ENERGIA ACTIVA", 3));
        System.out.println("Top 3 Barrios (ENERGIA REACTIVA): " + 
                estadisticas.getBarriosTopConsumo(2020, "ENERGIA REACTIVA", 3));
        
        System.out.println("---- PREGUNTA 2: MEDIA DE CONSUMO DE EDIFICIOS ----");
        System.out.println("Media de consumo de edificios de clase ENERGIA ACTIVA: " + 
        		estadisticas.getMediaConsumoEdificios("ENERGIA ACTIVA"));
        System.out.println("Media de consumo de edificios de clase GAS: " + 
                estadisticas.getMediaConsumoEdificios("GAS"));
        System.out.println("Media de consumo de edificios de clase ENERGIA REACTIVA: " + 
                estadisticas.getMediaConsumoEdificios("ENERGIA REACTIVA"));
        
        System.out.println("---- PREGUNTA 3: MEDIA DE CONSUMO POR TIPO DE EDIFICIO EN 2020 ----");
        System.out.println("Media de consumo de GAS por tipo de edificio en 2020: " +
        		estadisticas.getMediaConsumosDeEdificioPorTipo(2020, "GAS"));
        System.out.println("Media de consumo de ENERGIA ACTIVA por tipo de edificio en 2020: " +
        		estadisticas.getMediaConsumosDeEdificioPorTipo(2020, "ENERGIA ACTIVA"));
        System.out.println("Media de consumo de ENERGIA REACTIVA por tipo de edificio en 2020: " +
        		estadisticas.getMediaConsumosDeEdificioPorTipo(2020, "ENERGIA REACTIVA"));
        
        System.out.println("---- PREGUNTA 4: INCREMENTO DE CONSUMO ANUAL ----");
        System.out.println("Incremento de consumo anual por kWh: " +
        		estadisticas.incrementoAnualDeConsumoPorUnidad("kWh"));
        System.out.println("Incremento de consumo anual por m3: " +
        		estadisticas.incrementoAnualDeConsumoPorUnidad("m3"));
        System.out.println("Incremento de consumo anual por KVAr: " +
        		estadisticas.incrementoAnualDeConsumoPorUnidad("kVAr"));
	}
	
}

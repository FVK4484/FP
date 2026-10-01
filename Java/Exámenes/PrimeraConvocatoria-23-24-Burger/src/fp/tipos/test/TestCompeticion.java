package fp.tipos.test;

import java.time.Duration;
import java.time.LocalDate;
import java.util.Map;
import java.util.SortedSet;

import fp.tipos.Competicion;
import fp.tipos.FactoriaVisitas;
import fp.tipos.Visita;

public class TestCompeticion {
	public static void main(String[] args) {
		Competicion competicion = FactoriaVisitas.leeCompeticion("./data/evaluaciones.csv");
		System.out.println("FACTORÍA"+" =".repeat(80));
		testCreaCompeticionBurger(competicion);
		System.out.println("\nEJ1"+" =".repeat(80));
		testGetEmailsOrdenados(competicion, Duration.ofMinutes(240));
		testGetEmailsOrdenados (competicion, Duration.ofMinutes(300));
		System.out.println("\nEJ2"+" =".repeat(80));
		testGetTotalVisitasComilones(competicion);
		System.out.println("\nEJ3"+" =".repeat(80));
		testGetPeorHamburgueseriaPorCalidadIngredientes(competicion);
		System.out.println("\nEJ4"+" =".repeat(80));
		testGetTopComilonPorCPEnDia(competicion, LocalDate.of(2024, 6, 2));
		System.out.println("\nEJ5"+" =".repeat(80));
		testGetHamburgueseriaGanadora(competicion);
	}
	private static void testCreaCompeticionBurger(Competicion comp) {
		try {
			SortedSet<Visita> visitas = comp.getVisitas();
			System.out.println(String.format("Leidas %d visitas", visitas.size()));
			System.out.println("Primera visita: "+ visitas.first()+"\n");
			System.out.println("Última visita: "+ visitas.last());
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
	private static void testGetEmailsOrdenados(Competicion comp, Duration d) {
		try {
			SortedSet<String> res = comp.getEmailsOrdenados(d);
			String msg = String.format(
					"Los emails de las visitas con duración mayor a %d minutos son:\n%s",
					d.toMinutes(), res);
			System.out.println(msg);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
	private static void testGetTotalVisitasComilones(Competicion comp) {
		try {
			Integer res = comp.getTotalVisitasComilones();
			String msg = String.format(
					"El total de visitas con un nº de evaluaciones mayor a la media es:\n%d",
					res);
			System.out.println(msg);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
	private static void testGetPeorHamburgueseriaPorCalidadIngredientes(Competicion comp) {
		try {
			String res = comp.getPeorHamburgueseriaPorCalidadIngredientes();
			String msg = String.format(
					"Si se tiene en cuenta solo la calidad de ingredientes" +
							", la peor hamburguesería es:\n%s", res);
			System.out.println(msg);
			} catch (Exception e) {
				System.out.println(e.getMessage());
			}
			}
			private static void testGetTopComilonPorCPEnDia(Competicion comp, LocalDate f) {
				try {
					Map<String, String> res = comp.getTopComilonPorCPEnDia(f);
					String msg = String.format(
							"En el día %s la persona que más comió de cada CP es:\n%s",
							f, res);
					System.out.println(msg);
				} catch (Exception e) {
					System.out.println(e.getMessage());
				}
			}
			private static void testGetHamburgueseriaGanadora(Competicion comp) {
				try {
					String res = comp.getHamburgueseriaGanadora();
					String msg = String.format("La hamburguesería ganadora del campeonato es:\n%s",
							res);
					System.out.println(msg);
				} catch (Exception e) {
					System.out.println(e.getMessage());
					}
				}
}
